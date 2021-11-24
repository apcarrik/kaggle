def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]>1:
		# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[10]<=3.0:
			# {"feature": "Bar", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[8]<=2.0:
				return 'True'
			elif obj[8]>2.0:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[10]>3.0:
			return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 2}
		if obj[1]>0:
			# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[6]>0:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[9]<=3.0:
						return 'False'
					elif obj[9]>3.0:
						return 'True'
					else: return 'True'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[6]<=0:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'

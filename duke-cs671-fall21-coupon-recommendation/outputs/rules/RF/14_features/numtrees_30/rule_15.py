def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[8]>2:
		# {"feature": "Gender", "instances": 19, "metric_value": 0.7425, "depth": 2}
		if obj[3]<=0:
			# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[9]>0.0:
				# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[1]>2:
					return 'False'
				elif obj[1]<=2:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[3]>0:
			return 'True'
		else: return 'True'
	elif obj[8]<=2:
		# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[10]<=2.0:
			# {"feature": "Age", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[4]>0:
				return 'False'
			elif obj[4]<=0:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=0:
						return 'True'
					elif obj[5]>0:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[10]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'

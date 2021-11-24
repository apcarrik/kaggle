def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[6]<=1:
		# {"feature": "Passanger", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[5]>0:
						return 'False'
					elif obj[5]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]>2:
				# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]<=3:
					return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	elif obj[6]>1:
		# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[9]<=1.0:
			return 'False'
		elif obj[9]>1.0:
			# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

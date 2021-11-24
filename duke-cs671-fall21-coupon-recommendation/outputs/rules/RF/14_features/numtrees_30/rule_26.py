def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[6]<=1:
		# {"feature": "Passanger", "instances": 18, "metric_value": 0.5033, "depth": 2}
		if obj[0]>1:
			return 'True'
		elif obj[0]<=1:
			# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=0:
					return 'False'
				elif obj[3]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[6]>1:
		# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[10]>1.0:
			# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[13]<=1:
					return 'True'
				elif obj[13]>1:
					# {"feature": "Income", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[8]<=0:
						return 'True'
					elif obj[8]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[10]<=1.0:
			return 'False'
		else: return 'False'
	else: return 'False'

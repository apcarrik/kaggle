def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[2]<=14:
		# {"feature": "Education", "instances": 47, "metric_value": 0.9035, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Restaurant20to50", "instances": 44, "metric_value": 0.9257, "depth": 3}
			if obj[3]<=3.0:
				# {"feature": "Coupon", "instances": 43, "metric_value": 0.9103, "depth": 4}
				if obj[0]>2:
					# {"feature": "Distance", "instances": 25, "metric_value": 0.971, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[0]<=2:
					# {"feature": "Distance", "instances": 18, "metric_value": 0.7642, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>3.0:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[2]>14:
		return 'False'
	else: return 'False'

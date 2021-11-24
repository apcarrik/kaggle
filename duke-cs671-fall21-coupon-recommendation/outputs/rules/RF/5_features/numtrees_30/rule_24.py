def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.8338, "depth": 1}
	if obj[0]>1:
		# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.7355, "depth": 2}
		if obj[3]<=1.0:
			# {"feature": "Education", "instances": 20, "metric_value": 0.8813, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[2]>4:
					# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[2]<=4:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[3]>1.0:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 2}
		if obj[4]<=2:
			return 'False'
		elif obj[4]>2:
			return 'True'
		else: return 'True'
	else: return 'False'

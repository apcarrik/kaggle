def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.7425, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[4]>1:
					# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					return 'False'
				else: return 'False'
			elif obj[3]>2.0:
				return 'True'
			else: return 'True'
		elif obj[0]>3:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'

def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[0]>0:
		# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.9871, "depth": 2}
		if obj[3]>0.0:
			# {"feature": "Occupation", "instances": 25, "metric_value": 0.9988, "depth": 3}
			if obj[2]<=16:
				# {"feature": "Education", "instances": 22, "metric_value": 0.976, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]>16:
				return 'True'
			else: return 'True'
		elif obj[3]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'

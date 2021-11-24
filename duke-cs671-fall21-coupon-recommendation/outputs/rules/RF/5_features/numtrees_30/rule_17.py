def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[2]>1:
		# {"feature": "Distance", "instances": 27, "metric_value": 0.999, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 3}
			if obj[0]>0:
				# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.8524, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]>1.0:
					# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[0]<=0:
				# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]<=2:
					return 'False'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>2:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		return 'True'
	else: return 'True'

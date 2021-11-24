def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 39, "metric_value": 0.9418, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.971, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Distance", "instances": 32, "metric_value": 0.9887, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Occupation", "instances": 31, "metric_value": 0.9932, "depth": 5}
					if obj[2]>5:
						return 'True'
					elif obj[2]<=5:
						return 'False'
					else: return 'False'
				elif obj[4]>2:
					return 'True'
				else: return 'True'
			elif obj[3]>2.0:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[2]>5:
				# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[4]>1:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					return 'False'
				else: return 'False'
			elif obj[2]<=5:
				return 'False'
			else: return 'False'
		elif obj[1]>0:
			return 'False'
		else: return 'False'
	else: return 'False'

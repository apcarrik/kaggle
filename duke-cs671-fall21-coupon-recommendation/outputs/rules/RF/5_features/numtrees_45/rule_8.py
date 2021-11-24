def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]<=1.0:
		# {"feature": "Education", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[2]<=7:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[0]>0:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[2]>7:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[0]>3:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[0]<=3:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[3]>1.0:
		return 'True'
	else: return 'True'

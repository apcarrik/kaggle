def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[2]<=14.152341062546483:
		# {"feature": "Distance", "instances": 43, "metric_value": 0.9996, "depth": 2}
		if obj[4]<=1:
			# {"feature": "Education", "instances": 24, "metric_value": 0.8709, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.9024, "depth": 4}
				if obj[3]<=2.0:
					# {"feature": "Coupon", "instances": 21, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]>2.0:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[4]>1:
			# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.8315, "depth": 3}
			if obj[3]<=1.0:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[0]>1:
					# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			elif obj[3]>1.0:
				# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[0]<=3:
						return 'True'
					elif obj[0]>3:
						return 'False'
					else: return 'False'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[2]>14.152341062546483:
		return 'False'
	else: return 'False'

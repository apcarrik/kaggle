def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[4]<=1.0:
		# {"feature": "Coupon", "instances": 15, "metric_value": 0.9968, "depth": 2}
		if obj[1]>3:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[3]<=14:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[0]>1:
					return 'False'
				elif obj[0]<=1:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[3]>14:
				return 'True'
			else: return 'True'
		elif obj[1]<=3:
			# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[5]>1:
				# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=1:
							return 'True'
						elif obj[3]>1:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[5]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[4]>1.0:
		# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[3]>0:
			return 'True'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'

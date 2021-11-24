def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[3]<=14:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[1]>1:
			# {"feature": "Education", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[2]>0:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[5]>1:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[0]>1:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'False'
						else: return 'False'
					elif obj[0]<=1:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>1.0:
							return 'True'
						elif obj[4]<=1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]>0:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=2.0:
							return 'True'
						else: return 'True'
					elif obj[5]>2:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]>14:
		return 'False'
	else: return 'False'

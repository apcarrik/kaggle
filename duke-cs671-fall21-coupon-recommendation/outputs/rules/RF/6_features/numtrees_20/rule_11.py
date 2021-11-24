def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[5]<=2:
		# {"feature": "Passanger", "instances": 46, "metric_value": 0.9503, "depth": 2}
		if obj[0]>0:
			# {"feature": "Restaurant20to50", "instances": 41, "metric_value": 0.9789, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Occupation", "instances": 30, "metric_value": 0.9968, "depth": 5}
					if obj[3]<=11:
						# {"feature": "Coupon", "instances": 24, "metric_value": 0.995, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[3]>11:
						# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[1]<=2:
							return 'False'
						elif obj[1]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[4]<=0.0:
				# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	elif obj[5]>2:
		return 'False'
	else: return 'False'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 22, "metric_value": 0.976, "depth": 2}
		if obj[3]<=6:
			# {"feature": "Direction_same", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[2]<=1:
					# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[1]>2:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=2:
								return 'False'
							else: return 'False'
						elif obj[4]>1.0:
							return 'False'
						else: return 'False'
					elif obj[1]<=2:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]>1:
					return 'True'
				else: return 'True'
			elif obj[5]>0:
				return 'False'
			else: return 'False'
		elif obj[3]>6:
			# {"feature": "Direction_same", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[5]<=0:
				return 'False'
			elif obj[5]>0:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[3]<=10:
				return 'True'
			elif obj[3]>10:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=0:
					return 'True'
				elif obj[2]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=6:
				return 'False'
			elif obj[3]>6:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'

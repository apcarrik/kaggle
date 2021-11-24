def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 48, "metric_value": 0.9183, "depth": 2}
		if obj[3]<=20:
			# {"feature": "Restaurant20to50", "instances": 46, "metric_value": 0.8865, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Education", "instances": 42, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Distance", "instances": 33, "metric_value": 0.8454, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Coupon", "instances": 27, "metric_value": 0.7642, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Direction_same", "instances": 14, "metric_value": 0.5917, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Direction_same", "instances": 13, "metric_value": 0.8905, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]>2:
						# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]>2:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[1]>1:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[1]<=1:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]>2.0:
				return 'True'
			else: return 'True'
		elif obj[3]>20:
			return 'False'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'

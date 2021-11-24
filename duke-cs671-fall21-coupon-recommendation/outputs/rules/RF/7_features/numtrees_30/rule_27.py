def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[3]<=7:
			# {"feature": "Coupon", "instances": 20, "metric_value": 0.9928, "depth": 3}
			if obj[1]>0:
				# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9641, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Distance", "instances": 16, "metric_value": 0.9887, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Education", "instances": 15, "metric_value": 0.9968, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[2]>2:
							# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[6]>2:
						return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[3]>7:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[2]>1:
						return 'False'
					elif obj[2]<=1:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]>0:
							return 'False'
						elif obj[5]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]>1.0:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=0:
		return 'True'
	else: return 'True'

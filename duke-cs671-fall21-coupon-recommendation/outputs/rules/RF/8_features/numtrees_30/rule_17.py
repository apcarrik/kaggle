def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[1]>0:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.9183, "depth": 2}
		if obj[3]<=21:
			# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.8865, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Passanger", "instances": 22, "metric_value": 0.8454, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Distance", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[7]<=2:
						# {"feature": "Bar", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[2]>3:
								return 'True'
							else: return 'True'
						elif obj[4]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[7]>2:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=0:
							return 'False'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[5]>2.0:
				return 'False'
			else: return 'False'
		elif obj[3]>21:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[0]<=1:
			return 'False'
		elif obj[0]>1:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]>0:
				return 'True'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

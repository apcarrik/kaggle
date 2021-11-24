def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]>0:
		# {"feature": "Coupon", "instances": 31, "metric_value": 0.9992, "depth": 2}
		if obj[2]>2:
			# {"feature": "Occupation", "instances": 17, "metric_value": 0.9367, "depth": 3}
			if obj[4]>5:
				# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[3]>1:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[8]>1:
						# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[1]>1:
							# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]>0.0:
									return 'True'
								elif obj[6]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[1]<=1:
							return 'False'
						else: return 'False'
					elif obj[8]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]<=1:
					# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[5]<=3.0:
						return 'True'
					elif obj[5]>3.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]<=5:
				return 'True'
			else: return 'True'
		elif obj[2]<=2:
			# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[3]<=4:
				# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[6]<=1.0:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[4]<=16:
						# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[1]>0:
							# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[8]<=2:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[5]>0.0:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[5]<=0.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]>2:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					elif obj[4]>16:
						return 'False'
					else: return 'False'
				elif obj[6]>1.0:
					return 'False'
				else: return 'False'
			elif obj[3]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=0:
		return 'True'
	else: return 'True'

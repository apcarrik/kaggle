def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[3]<=3:
		# {"feature": "Bar", "instances": 80, "metric_value": 0.9959, "depth": 2}
		if obj[5]<=1.0:
			# {"feature": "Coupon", "instances": 55, "metric_value": 0.9457, "depth": 3}
			if obj[2]>0:
				# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.8974, "depth": 4}
				if obj[6]<=1.0:
					# {"feature": "Distance", "instances": 33, "metric_value": 0.9834, "depth": 5}
					if obj[8]<=2:
						# {"feature": "Occupation", "instances": 31, "metric_value": 0.9629, "depth": 6}
						if obj[4]<=10:
							# {"feature": "Time", "instances": 24, "metric_value": 0.8709, "depth": 7}
							if obj[1]>0:
								# {"feature": "Passanger", "instances": 20, "metric_value": 0.9341, "depth": 8}
								if obj[0]>0:
									# {"feature": "Direction_same", "instances": 19, "metric_value": 0.9495, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						elif obj[4]>10:
							# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[0]>1:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[0]<=1:
									return 'False'
								else: return 'False'
							elif obj[1]>3:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[8]>2:
						return 'False'
					else: return 'False'
				elif obj[6]>1.0:
					# {"feature": "Passanger", "instances": 18, "metric_value": 0.5033, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[8]>1:
							# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[4]<=7:
									return 'True'
								elif obj[4]>7:
									return 'False'
								else: return 'False'
							elif obj[1]>1:
								return 'False'
							else: return 'False'
						elif obj[8]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[5]>1.0:
			# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.9044, "depth": 3}
			if obj[6]>-1.0:
				# {"feature": "Occupation", "instances": 23, "metric_value": 0.8281, "depth": 4}
				if obj[4]<=19:
					# {"feature": "Time", "instances": 22, "metric_value": 0.7732, "depth": 5}
					if obj[1]>0:
						# {"feature": "Passanger", "instances": 18, "metric_value": 0.65, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 14, "metric_value": 0.7496, "depth": 7}
							if obj[7]<=0:
								# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 8}
								if obj[2]>0:
									# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[8]<=2:
										return 'False'
									elif obj[8]>2:
										return 'False'
									else: return 'False'
								elif obj[2]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]>0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]>0:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>2:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[2]<=2:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]>19:
					return 'True'
				else: return 'True'
			elif obj[6]<=-1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]>3:
		return 'True'
	else: return 'True'

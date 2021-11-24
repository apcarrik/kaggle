def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 35, "metric_value": 0.9518, "depth": 2}
		if obj[3]>0:
			# {"feature": "Occupation", "instances": 22, "metric_value": 0.7732, "depth": 3}
			if obj[4]<=12:
				# {"feature": "Time", "instances": 19, "metric_value": 0.6292, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.6962, "depth": 5}
					if obj[6]>0.0:
						# {"feature": "Direction_same", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[7]<=0:
							# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[0]>1:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]>1:
										return 'True'
									elif obj[8]<=1:
										return 'True'
									else: return 'True'
								elif obj[5]>0.0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]>1:
										return 'True'
									elif obj[8]<=1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[0]<=1:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[8]<=1:
									return 'True'
								elif obj[8]>1:
									# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5]<=0.0:
										return 'False'
									elif obj[5]>0.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[7]>0:
							return 'True'
						else: return 'True'
					elif obj[6]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[4]>12:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=3:
					return 'False'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]<=0:
			# {"feature": "Bar", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[5]<=0.0:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[4]<=6:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[1]<=2:
							return 'False'
						elif obj[1]>2:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=2:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]>6:
					return 'True'
				else: return 'True'
			elif obj[5]>0.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Passanger", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[0]>0:
			# {"feature": "Bar", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[5]<=2.0:
				return 'False'
			elif obj[5]>2.0:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'

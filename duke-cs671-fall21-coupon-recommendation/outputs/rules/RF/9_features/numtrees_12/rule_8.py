def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9774, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Passanger", "instances": 64, "metric_value": 0.8774, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Coupon", "instances": 46, "metric_value": 0.9656, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Occupation", "instances": 33, "metric_value": 0.885, "depth": 4}
				if obj[4]<=19:
					# {"feature": "Bar", "instances": 32, "metric_value": 0.8571, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.65, "depth": 6}
						if obj[6]>-1.0:
							# {"feature": "Time", "instances": 17, "metric_value": 0.5226, "depth": 7}
							if obj[1]>1:
								return 'True'
							elif obj[1]<=1:
								# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[8]<=2:
									# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[8]>2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]<=-1.0:
							return 'False'
						else: return 'False'
					elif obj[5]<=0.0:
						# {"feature": "Distance", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[8]>1:
							# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[1]>0:
								# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=1.0:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[6]>1.0:
									return 'False'
								else: return 'False'
							elif obj[1]<=0:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=1.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[6]>1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[8]<=1:
							# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=1.0:
									return 'True'
								elif obj[6]>1.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>19:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				# {"feature": "Bar", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[5]<=0.0:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[4]>10:
						# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[1]<=0:
							return 'False'
						elif obj[1]>0:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]<=10:
						return 'True'
					else: return 'True'
				elif obj[5]>0.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[0]>2:
			# {"feature": "Time", "instances": 18, "metric_value": 0.3095, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[3]>2:
		# {"feature": "Coupon", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Distance", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[8]<=2:
				return 'False'
			elif obj[8]>2:
				return 'True'
			else: return 'True'
		elif obj[2]>3:
			# {"feature": "Time", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[1]>1:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[4]>7:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>2:
						return 'False'
					elif obj[0]<=2:
						return 'True'
					else: return 'True'
				elif obj[4]<=7:
					return 'True'
				else: return 'True'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9566, "depth": 1}
	if obj[2]>1:
		# {"feature": "Passanger", "instances": 96, "metric_value": 0.8571, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Restaurant20to50", "instances": 64, "metric_value": 0.9544, "depth": 3}
			if obj[6]<=2.0:
				# {"feature": "Education", "instances": 59, "metric_value": 0.9748, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Occupation", "instances": 48, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=12:
						# {"feature": "Distance", "instances": 41, "metric_value": 0.8722, "depth": 6}
						if obj[8]>1:
							# {"feature": "Bar", "instances": 26, "metric_value": 0.9612, "depth": 7}
							if obj[5]<=2.0:
								# {"feature": "Direction_same", "instances": 23, "metric_value": 0.8865, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Time", "instances": 20, "metric_value": 0.9341, "depth": 9}
									if obj[1]<=3:
										return 'True'
									elif obj[1]>3:
										return 'True'
									else: return 'True'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							elif obj[5]>2.0:
								return 'False'
							else: return 'False'
						elif obj[8]<=1:
							# {"feature": "Direction_same", "instances": 15, "metric_value": 0.5665, "depth": 7}
							if obj[7]<=0:
								return 'True'
							elif obj[7]>0:
								# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=1.0:
									# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[1]<=1:
										return 'True'
									elif obj[1]>1:
										return 'False'
									else: return 'False'
								elif obj[5]>1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]>12:
						# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[8]<=2:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[7]>0:
									# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[7]<=0:
									return 'False'
								else: return 'False'
							elif obj[8]>2:
								return 'True'
							else: return 'True'
						elif obj[1]>3:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]>2:
					# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[8]>1:
							return 'False'
						elif obj[8]<=1:
							# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]>4:
								return 'False'
							elif obj[4]<=4:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[1]>1:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>3:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=1.0:
								return 'False'
							elif obj[5]>1.0:
								return 'True'
							else: return 'True'
						elif obj[4]<=3:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]>2.0:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 32, "metric_value": 0.4489, "depth": 3}
			if obj[4]<=5:
				# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.65, "depth": 4}
				if obj[6]<=3.0:
					# {"feature": "Time", "instances": 17, "metric_value": 0.5226, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[3]>0:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									return 'True'
								else: return 'True'
							elif obj[3]<=0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[8]>1:
									return 'True'
								elif obj[8]<=1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[5]>0.0:
							return 'True'
						else: return 'True'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[6]>3.0:
					return 'False'
				else: return 'False'
			elif obj[4]>5:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.9072, "depth": 2}
		if obj[4]>2:
			# {"feature": "Bar", "instances": 25, "metric_value": 0.7219, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Education", "instances": 24, "metric_value": 0.65, "depth": 4}
				if obj[3]<=3:
					# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.469, "depth": 5}
					if obj[6]<=1.0:
						# {"feature": "Time", "instances": 14, "metric_value": 0.5917, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Distance", "instances": 11, "metric_value": 0.684, "depth": 7}
							if obj[8]<=2:
								# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[7]>0:
										return 'False'
									elif obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[0]>1:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[8]>2:
								return 'False'
							else: return 'False'
						elif obj[1]>3:
							return 'False'
						else: return 'False'
					elif obj[6]>1.0:
						return 'False'
					else: return 'False'
				elif obj[3]>3:
					# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]>2.0:
				return 'True'
			else: return 'True'
		elif obj[4]<=2:
			# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

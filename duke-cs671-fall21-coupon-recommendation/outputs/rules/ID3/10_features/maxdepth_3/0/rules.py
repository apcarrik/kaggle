def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4744, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 5889, "metric_value": 0.4587, "depth": 2}
		if obj[6]>0.0:
			# {"feature": "Distance", "instances": 4432, "metric_value": 0.4358, "depth": 3}
			if obj[9]<=2:
				# {"feature": "Passanger", "instances": 4015, "metric_value": 0.4266, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Time", "instances": 2626, "metric_value": 0.4479, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Occupation", "instances": 2123, "metric_value": 0.4553, "depth": 6}
						if obj[4]>0:
							# {"feature": "Direction_same", "instances": 2109, "metric_value": 0.4565, "depth": 7}
							if obj[8]<=0:
								# {"feature": "Restaurant20to50", "instances": 1161, "metric_value": 0.4673, "depth": 8}
								if obj[7]<=3.0:
									# {"feature": "Education", "instances": 1126, "metric_value": 0.4704, "depth": 9}
									if obj[3]<=3:
										# {"feature": "Bar", "instances": 1058, "metric_value": 0.4722, "depth": 10}
										if obj[5]>0.0:
											return 'True'
										elif obj[5]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[3]>3:
										# {"feature": "Bar", "instances": 68, "metric_value": 0.4281, "depth": 10}
										if obj[5]<=2.0:
											return 'True'
										elif obj[5]>2.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>3.0:
									# {"feature": "Bar", "instances": 35, "metric_value": 0.3255, "depth": 9}
									if obj[5]>2.0:
										# {"feature": "Education", "instances": 22, "metric_value": 0.4329, "depth": 10}
										if obj[3]>1:
											return 'True'
										elif obj[3]<=1:
											return 'True'
										else: return 'True'
									elif obj[5]<=2.0:
										# {"feature": "Education", "instances": 13, "metric_value": 0.1346, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]>0:
								# {"feature": "Bar", "instances": 948, "metric_value": 0.4386, "depth": 8}
								if obj[5]>-1.0:
									# {"feature": "Restaurant20to50", "instances": 940, "metric_value": 0.4379, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Education", "instances": 841, "metric_value": 0.4443, "depth": 10}
										if obj[3]<=2:
											return 'True'
										elif obj[3]>2:
											return 'True'
										else: return 'True'
									elif obj[7]>2.0:
										# {"feature": "Education", "instances": 99, "metric_value": 0.3718, "depth": 10}
										if obj[3]<=2:
											return 'True'
										elif obj[3]>2:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]<=-1.0:
									# {"feature": "Education", "instances": 8, "metric_value": 0.375, "depth": 9}
									if obj[3]<=1:
										# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[7]<=1.0:
											return 'False'
										else: return 'False'
									elif obj[3]>1:
										# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[7]<=2.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[4]<=0:
							# {"feature": "Education", "instances": 14, "metric_value": 0.1143, "depth": 7}
							if obj[3]<=0:
								return 'True'
							elif obj[3]>0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2667, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[5]<=2.0:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[7]<=1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[1]>3:
						# {"feature": "Bar", "instances": 503, "metric_value": 0.4078, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Occupation", "instances": 337, "metric_value": 0.3791, "depth": 7}
							if obj[4]<=13.168241765136806:
								# {"feature": "Education", "instances": 281, "metric_value": 0.3606, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Restaurant20to50", "instances": 268, "metric_value": 0.3706, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 182, "metric_value": 0.3831, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Direction_same", "instances": 86, "metric_value": 0.3442, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>3:
									# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.1399, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 11, "metric_value": 0.1653, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]>13.168241765136806:
								# {"feature": "Education", "instances": 56, "metric_value": 0.4456, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Restaurant20to50", "instances": 42, "metric_value": 0.4179, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Direction_same", "instances": 40, "metric_value": 0.4387, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>2.0:
										return 'True'
									else: return 'True'
								elif obj[3]>2:
									# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.45, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]<=0.0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]>1.0:
							# {"feature": "Education", "instances": 166, "metric_value": 0.4524, "depth": 7}
							if obj[3]>0:
								# {"feature": "Occupation", "instances": 115, "metric_value": 0.4565, "depth": 8}
								if obj[4]<=19:
									# {"feature": "Restaurant20to50", "instances": 112, "metric_value": 0.4647, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 103, "metric_value": 0.4751, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>19:
									return 'False'
								else: return 'False'
							elif obj[3]<=0:
								# {"feature": "Occupation", "instances": 51, "metric_value": 0.3037, "depth": 8}
								if obj[4]>4:
									# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.2501, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 22, "metric_value": 0.1653, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Direction_same", "instances": 17, "metric_value": 0.3599, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=4:
									# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4242, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4628, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]>1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Occupation", "instances": 1389, "metric_value": 0.382, "depth": 5}
					if obj[4]<=18.52567473260329:
						# {"feature": "Bar", "instances": 1292, "metric_value": 0.3906, "depth": 6}
						if obj[5]<=3.0:
							# {"feature": "Restaurant20to50", "instances": 1225, "metric_value": 0.3841, "depth": 7}
							if obj[7]<=1.0:
								# {"feature": "Education", "instances": 789, "metric_value": 0.4048, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Time", "instances": 745, "metric_value": 0.4128, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 580, "metric_value": 0.4101, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										# {"feature": "Direction_same", "instances": 165, "metric_value": 0.4224, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>3:
									# {"feature": "Time", "instances": 44, "metric_value": 0.2645, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 33, "metric_value": 0.2975, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										# {"feature": "Direction_same", "instances": 11, "metric_value": 0.1653, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]>1.0:
								# {"feature": "Time", "instances": 436, "metric_value": 0.3377, "depth": 8}
								if obj[1]>0:
									# {"feature": "Education", "instances": 337, "metric_value": 0.373, "depth": 9}
									if obj[3]<=3:
										# {"feature": "Direction_same", "instances": 317, "metric_value": 0.3805, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]>3:
										# {"feature": "Direction_same", "instances": 20, "metric_value": 0.255, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Education", "instances": 99, "metric_value": 0.2115, "depth": 9}
									if obj[3]<=3:
										# {"feature": "Direction_same", "instances": 94, "metric_value": 0.2227, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]>3:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]>3.0:
							# {"feature": "Time", "instances": 67, "metric_value": 0.4397, "depth": 7}
							if obj[1]>0:
								# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.4057, "depth": 8}
								if obj[7]>2.0:
									# {"feature": "Education", "instances": 26, "metric_value": 0.4253, "depth": 9}
									if obj[3]>3:
										# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4152, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]<=3:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]<=2.0:
									# {"feature": "Education", "instances": 25, "metric_value": 0.3, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Direction_same", "instances": 16, "metric_value": 0.2188, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Education", "instances": 16, "metric_value": 0.4563, "depth": 8}
								if obj[3]>0:
									# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.4167, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.3429, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]>2.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]>18.52567473260329:
						# {"feature": "Bar", "instances": 97, "metric_value": 0.2374, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Restaurant20to50", "instances": 69, "metric_value": 0.2928, "depth": 7}
							if obj[7]<=1.0:
								# {"feature": "Time", "instances": 62, "metric_value": 0.2567, "depth": 8}
								if obj[1]>0:
									# {"feature": "Education", "instances": 49, "metric_value": 0.3174, "depth": 9}
									if obj[3]<=2:
										# {"feature": "Direction_same", "instances": 38, "metric_value": 0.3615, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]>2:
										# {"feature": "Direction_same", "instances": 11, "metric_value": 0.1653, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]>1.0:
								# {"feature": "Education", "instances": 7, "metric_value": 0.2143, "depth": 8}
								if obj[3]>0:
									# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]>1.0:
							# {"feature": "Education", "instances": 28, "metric_value": 0.0663, "depth": 7}
							if obj[3]>0:
								# {"feature": "Time", "instances": 14, "metric_value": 0.1224, "depth": 8}
								if obj[1]<=2:
									return 'True'
								elif obj[1]>2:
									# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2286, "depth": 9}
									if obj[7]>1.0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[9]>2:
				# {"feature": "Passanger", "instances": 417, "metric_value": 0.4857, "depth": 4}
				if obj[0]>0:
					# {"feature": "Time", "instances": 404, "metric_value": 0.4863, "depth": 5}
					if obj[1]>0:
						# {"feature": "Bar", "instances": 347, "metric_value": 0.4936, "depth": 6}
						if obj[5]>-1.0:
							# {"feature": "Education", "instances": 344, "metric_value": 0.4944, "depth": 7}
							if obj[3]<=3:
								# {"feature": "Restaurant20to50", "instances": 318, "metric_value": 0.4935, "depth": 8}
								if obj[7]>-1.0:
									# {"feature": "Occupation", "instances": 316, "metric_value": 0.495, "depth": 9}
									if obj[4]<=7.639240506329114:
										# {"feature": "Direction_same", "instances": 202, "metric_value": 0.4992, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[4]>7.639240506329114:
										# {"feature": "Direction_same", "instances": 114, "metric_value": 0.4875, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[3]>3:
								# {"feature": "Occupation", "instances": 26, "metric_value": 0.337, "depth": 8}
								if obj[4]>1:
									# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.2286, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										return 'True'
									else: return 'True'
								elif obj[4]<=1:
									# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.3704, "depth": 9}
									if obj[7]<=3.0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]>3.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[5]<=-1.0:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						# {"feature": "Education", "instances": 57, "metric_value": 0.3851, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Bar", "instances": 43, "metric_value": 0.4289, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Occupation", "instances": 29, "metric_value": 0.3557, "depth": 8}
								if obj[4]>2:
									# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.3021, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 16, "metric_value": 0.2188, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]>1.0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]<=2:
									# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.4, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[5]<=0.0:
								# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.3365, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Occupation", "instances": 9, "metric_value": 0.0, "depth": 9}
									if obj[4]<=19:
										return 'True'
									elif obj[4]>19:
										return 'False'
									else: return 'False'
								elif obj[7]<=0.0:
									# {"feature": "Occupation", "instances": 5, "metric_value": 0.0, "depth": 9}
									if obj[4]>1:
										return 'False'
									elif obj[4]<=1:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[3]>2:
							# {"feature": "Occupation", "instances": 14, "metric_value": 0.0, "depth": 7}
							if obj[4]<=16:
								return 'False'
							elif obj[4]>16:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[0]<=0:
					# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.2051, "depth": 5}
					if obj[7]<=1.0:
						return 'True'
					elif obj[7]>1.0:
						# {"feature": "Bar", "instances": 6, "metric_value": 0.0, "depth": 6}
						if obj[5]>1.0:
							return 'True'
						elif obj[5]<=1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]<=0.0:
			# {"feature": "Passanger", "instances": 1457, "metric_value": 0.495, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Distance", "instances": 933, "metric_value": 0.4888, "depth": 4}
				if obj[9]<=1:
					# {"feature": "Time", "instances": 499, "metric_value": 0.4911, "depth": 5}
					if obj[1]>0:
						# {"feature": "Direction_same", "instances": 325, "metric_value": 0.478, "depth": 6}
						if obj[8]>0:
							# {"feature": "Education", "instances": 170, "metric_value": 0.4853, "depth": 7}
							if obj[3]>1:
								# {"feature": "Restaurant20to50", "instances": 103, "metric_value": 0.4845, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Occupation", "instances": 101, "metric_value": 0.4875, "depth": 9}
									if obj[4]>5:
										# {"feature": "Bar", "instances": 61, "metric_value": 0.4748, "depth": 10}
										if obj[5]>0.0:
											return 'True'
										elif obj[5]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[4]<=5:
										# {"feature": "Bar", "instances": 40, "metric_value": 0.432, "depth": 10}
										if obj[5]<=0.0:
											return 'False'
										elif obj[5]>0.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]>2.0:
									return 'False'
								else: return 'False'
							elif obj[3]<=1:
								# {"feature": "Bar", "instances": 67, "metric_value": 0.4411, "depth": 8}
								if obj[5]<=1.0:
									# {"feature": "Restaurant20to50", "instances": 55, "metric_value": 0.3984, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Occupation", "instances": 46, "metric_value": 0.439, "depth": 10}
										if obj[4]<=12:
											return 'True'
										elif obj[4]>12:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										return 'True'
									else: return 'True'
								elif obj[5]>1.0:
									# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.3429, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Occupation", "instances": 7, "metric_value": 0.2286, "depth": 10}
										if obj[4]>1:
											return 'False'
										elif obj[4]<=1:
											return 'False'
										else: return 'False'
									elif obj[7]>1.0:
										# {"feature": "Occupation", "instances": 5, "metric_value": 0.4667, "depth": 10}
										if obj[4]>10:
											return 'True'
										elif obj[4]<=10:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[8]<=0:
							# {"feature": "Bar", "instances": 155, "metric_value": 0.4437, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "Occupation", "instances": 82, "metric_value": 0.3864, "depth": 8}
								if obj[4]<=6:
									# {"feature": "Education", "instances": 51, "metric_value": 0.4422, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.359, "depth": 10}
										if obj[7]<=1.0:
											return 'True'
										elif obj[7]>1.0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.4562, "depth": 10}
										if obj[7]>0.0:
											return 'True'
										elif obj[7]<=0.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]>6:
									# {"feature": "Education", "instances": 31, "metric_value": 0.2497, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.1042, "depth": 10}
										if obj[7]<=0.0:
											return 'True'
										elif obj[7]>0.0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.3778, "depth": 10}
										if obj[7]>0.0:
											return 'True'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[5]>0.0:
								# {"feature": "Restaurant20to50", "instances": 73, "metric_value": 0.447, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Occupation", "instances": 61, "metric_value": 0.4307, "depth": 9}
									if obj[4]<=6:
										# {"feature": "Education", "instances": 34, "metric_value": 0.4847, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[4]>6:
										# {"feature": "Education", "instances": 27, "metric_value": 0.3281, "depth": 10}
										if obj[3]>1:
											return 'True'
										elif obj[3]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]<=0.0:
									# {"feature": "Occupation", "instances": 12, "metric_value": 0.25, "depth": 9}
									if obj[4]>8:
										return 'False'
									elif obj[4]<=8:
										# {"feature": "Education", "instances": 6, "metric_value": 0.4, "depth": 10}
										if obj[3]<=2:
											return 'False'
										elif obj[3]>2:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Occupation", "instances": 174, "metric_value": 0.4654, "depth": 6}
						if obj[4]<=6:
							# {"feature": "Education", "instances": 94, "metric_value": 0.4397, "depth": 7}
							if obj[3]<=4:
								# {"feature": "Bar", "instances": 93, "metric_value": 0.4348, "depth": 8}
								if obj[5]>-1.0:
									# {"feature": "Restaurant20to50", "instances": 92, "metric_value": 0.4372, "depth": 9}
									if obj[7]>-1.0:
										# {"feature": "Direction_same", "instances": 91, "metric_value": 0.4405, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[7]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[5]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[3]>4:
								return 'True'
							else: return 'True'
						elif obj[4]>6:
							# {"feature": "Direction_same", "instances": 80, "metric_value": 0.4492, "depth": 7}
							if obj[8]>0:
								# {"feature": "Restaurant20to50", "instances": 42, "metric_value": 0.4, "depth": 8}
								if obj[7]>-1.0:
									# {"feature": "Bar", "instances": 40, "metric_value": 0.4154, "depth": 9}
									if obj[5]<=2.0:
										# {"feature": "Education", "instances": 39, "metric_value": 0.4251, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]>2.0:
										return 'True'
									else: return 'True'
								elif obj[7]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[8]<=0:
								# {"feature": "Education", "instances": 38, "metric_value": 0.4605, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Bar", "instances": 36, "metric_value": 0.4611, "depth": 9}
									if obj[5]<=2.0:
										# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.491, "depth": 10}
										if obj[7]<=1.0:
											return 'False'
										elif obj[7]>1.0:
											return 'True'
										else: return 'True'
									elif obj[5]>2.0:
										# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[7]>1.0:
											return 'False'
										elif obj[7]<=1.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>3:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[9]>1:
					# {"feature": "Education", "instances": 434, "metric_value": 0.4739, "depth": 5}
					if obj[3]>1:
						# {"feature": "Bar", "instances": 258, "metric_value": 0.4526, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Occupation", "instances": 202, "metric_value": 0.4655, "depth": 7}
							if obj[4]<=9:
								# {"feature": "Time", "instances": 134, "metric_value": 0.4758, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 107, "metric_value": 0.4829, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Restaurant20to50", "instances": 89, "metric_value": 0.4818, "depth": 10}
										if obj[7]>0.0:
											return 'False'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[8]>0:
										# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.3723, "depth": 10}
										if obj[7]<=1.0:
											return 'False'
										elif obj[7]>1.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]<=0:
									# {"feature": "Direction_same", "instances": 27, "metric_value": 0.3608, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.2647, "depth": 10}
										if obj[7]>0.0:
											return 'False'
										elif obj[7]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.4762, "depth": 10}
										if obj[7]>0.0:
											return 'False'
										elif obj[7]<=0.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[4]>9:
								# {"feature": "Direction_same", "instances": 68, "metric_value": 0.4059, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Time", "instances": 54, "metric_value": 0.3641, "depth": 9}
									if obj[1]>0:
										# {"feature": "Restaurant20to50", "instances": 47, "metric_value": 0.4144, "depth": 10}
										if obj[7]<=2.0:
											return 'False'
										elif obj[7]>2.0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[8]>0:
									# {"feature": "Time", "instances": 14, "metric_value": 0.381, "depth": 9}
									if obj[1]>0:
										# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.419, "depth": 10}
										if obj[7]>0.0:
											return 'False'
										elif obj[7]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[5]>1.0:
							# {"feature": "Occupation", "instances": 56, "metric_value": 0.3569, "depth": 7}
							if obj[4]>3:
								# {"feature": "Restaurant20to50", "instances": 43, "metric_value": 0.4027, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Time", "instances": 30, "metric_value": 0.4593, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Direction_same", "instances": 21, "metric_value": 0.4417, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[1]>1:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]>1.0:
									# {"feature": "Direction_same", "instances": 13, "metric_value": 0.141, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Time", "instances": 12, "metric_value": 0.1111, "depth": 10}
										if obj[1]<=1:
											return 'False'
										elif obj[1]>1:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[4]<=3:
								# {"feature": "Time", "instances": 13, "metric_value": 0.1282, "depth": 8}
								if obj[1]<=1:
									return 'False'
								elif obj[1]>1:
									# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.25, "depth": 9}
									if obj[7]>1.0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]<=1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]<=1:
						# {"feature": "Occupation", "instances": 176, "metric_value": 0.483, "depth": 6}
						if obj[4]>3:
							# {"feature": "Restaurant20to50", "instances": 115, "metric_value": 0.4881, "depth": 7}
							if obj[7]<=1.0:
								# {"feature": "Time", "instances": 89, "metric_value": 0.492, "depth": 8}
								if obj[1]>0:
									# {"feature": "Bar", "instances": 72, "metric_value": 0.4884, "depth": 9}
									if obj[5]<=2.0:
										# {"feature": "Direction_same", "instances": 65, "metric_value": 0.4941, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[5]>2.0:
										# {"feature": "Direction_same", "instances": 7, "metric_value": 0.3714, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[1]<=0:
									# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4189, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Bar", "instances": 11, "metric_value": 0.4545, "depth": 10}
										if obj[5]<=2.0:
											return 'True'
										elif obj[5]>2.0:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										# {"feature": "Bar", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[5]<=0.0:
											return 'True'
										elif obj[5]>0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]>1.0:
								# {"feature": "Time", "instances": 26, "metric_value": 0.4259, "depth": 8}
								if obj[1]>0:
									# {"feature": "Bar", "instances": 23, "metric_value": 0.3844, "depth": 9}
									if obj[5]>0.0:
										# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4613, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[5]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Bar", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[5]>0.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[8]>0:
											return 'True'
										elif obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[5]<=0.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[4]<=3:
							# {"feature": "Restaurant20to50", "instances": 61, "metric_value": 0.4312, "depth": 7}
							if obj[7]>0.0:
								# {"feature": "Direction_same", "instances": 41, "metric_value": 0.4253, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Time", "instances": 35, "metric_value": 0.4114, "depth": 9}
									if obj[1]>0:
										# {"feature": "Bar", "instances": 30, "metric_value": 0.4528, "depth": 10}
										if obj[5]<=1.0:
											return 'False'
										elif obj[5]>1.0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[8]>0:
									# {"feature": "Time", "instances": 6, "metric_value": 0.2222, "depth": 9}
									if obj[1]>0:
										# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[5]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]<=0.0:
								# {"feature": "Time", "instances": 20, "metric_value": 0.3, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Direction_same", "instances": 16, "metric_value": 0.3333, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Bar", "instances": 12, "metric_value": 0.4444, "depth": 10}
										if obj[5]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										return 'False'
									else: return 'False'
								elif obj[1]>3:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Distance", "instances": 524, "metric_value": 0.4635, "depth": 4}
				if obj[9]>1:
					# {"feature": "Occupation", "instances": 349, "metric_value": 0.4481, "depth": 5}
					if obj[4]>1.5048799563075503:
						# {"feature": "Time", "instances": 290, "metric_value": 0.4613, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Education", "instances": 169, "metric_value": 0.4664, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Restaurant20to50", "instances": 140, "metric_value": 0.4914, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Bar", "instances": 114, "metric_value": 0.4767, "depth": 9}
									if obj[5]<=2.0:
										# {"feature": "Direction_same", "instances": 110, "metric_value": 0.494, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]>2.0:
										return 'True'
									else: return 'True'
								elif obj[7]>1.0:
									# {"feature": "Bar", "instances": 26, "metric_value": 0.4796, "depth": 9}
									if obj[5]<=2.0:
										# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4983, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]>2.0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[3]>2:
								# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.3155, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Bar", "instances": 27, "metric_value": 0.2963, "depth": 9}
									if obj[5]<=2.0:
										# {"feature": "Direction_same", "instances": 24, "metric_value": 0.2778, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]>2.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>2.0:
									# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[5]<=0.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Restaurant20to50", "instances": 121, "metric_value": 0.4185, "depth": 7}
							if obj[7]<=1.0:
								# {"feature": "Education", "instances": 96, "metric_value": 0.4508, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Bar", "instances": 91, "metric_value": 0.444, "depth": 9}
									if obj[5]>-1.0:
										# {"feature": "Direction_same", "instances": 89, "metric_value": 0.454, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]<=-1.0:
										return 'True'
									else: return 'True'
								elif obj[3]>3:
									# {"feature": "Bar", "instances": 5, "metric_value": 0.2667, "depth": 9}
									if obj[5]<=0.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]>0.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]>1.0:
								# {"feature": "Education", "instances": 25, "metric_value": 0.24, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Bar", "instances": 20, "metric_value": 0.1444, "depth": 9}
									if obj[5]<=3.0:
										# {"feature": "Direction_same", "instances": 18, "metric_value": 0.1049, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]>3.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>2:
									# {"feature": "Bar", "instances": 5, "metric_value": 0.48, "depth": 9}
									if obj[5]<=0.0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]<=1.5048799563075503:
						# {"feature": "Time", "instances": 59, "metric_value": 0.3448, "depth": 6}
						if obj[1]>0:
							# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.399, "depth": 7}
							if obj[7]>0.0:
								# {"feature": "Education", "instances": 33, "metric_value": 0.3463, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Bar", "instances": 28, "metric_value": 0.4011, "depth": 9}
									if obj[5]<=2.0:
										# {"feature": "Direction_same", "instances": 26, "metric_value": 0.3935, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]>2.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>2:
									return 'True'
								else: return 'True'
							elif obj[7]<=0.0:
								# {"feature": "Education", "instances": 12, "metric_value": 0.375, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Bar", "instances": 8, "metric_value": 0.375, "depth": 9}
									if obj[5]<=0.0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>2:
									# {"feature": "Bar", "instances": 4, "metric_value": 0.0, "depth": 9}
									if obj[5]>-1.0:
										return 'False'
									elif obj[5]<=-1.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Education", "instances": 14, "metric_value": 0.125, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.2, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Bar", "instances": 5, "metric_value": 0.32, "depth": 9}
									if obj[5]<=0.0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>1.0:
									return 'True'
								else: return 'True'
							elif obj[3]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[9]<=1:
					# {"feature": "Occupation", "instances": 175, "metric_value": 0.4681, "depth": 5}
					if obj[4]>0:
						# {"feature": "Education", "instances": 171, "metric_value": 0.4675, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Restaurant20to50", "instances": 138, "metric_value": 0.4827, "depth": 7}
							if obj[7]>0.0:
								# {"feature": "Time", "instances": 97, "metric_value": 0.4603, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Bar", "instances": 69, "metric_value": 0.4857, "depth": 9}
									if obj[5]<=1.0:
										# {"feature": "Direction_same", "instances": 45, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[5]>1.0:
										# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4965, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>3:
									# {"feature": "Bar", "instances": 28, "metric_value": 0.3652, "depth": 9}
									if obj[5]<=2.0:
										# {"feature": "Direction_same", "instances": 23, "metric_value": 0.3403, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[5]>2.0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]<=0.0:
								# {"feature": "Bar", "instances": 41, "metric_value": 0.4671, "depth": 8}
								if obj[5]<=1.0:
									# {"feature": "Time", "instances": 35, "metric_value": 0.4959, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Direction_same", "instances": 28, "metric_value": 0.4974, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]>3:
										# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]>1.0:
									# {"feature": "Time", "instances": 6, "metric_value": 0.2222, "depth": 9}
									if obj[1]>3:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[1]<=3:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]>2:
							# {"feature": "Time", "instances": 33, "metric_value": 0.3561, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.3043, "depth": 8}
								if obj[7]>-1.0:
									# {"feature": "Bar", "instances": 23, "metric_value": 0.2849, "depth": 9}
									if obj[5]<=1.0:
										# {"feature": "Direction_same", "instances": 19, "metric_value": 0.2659, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[5]>1.0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]<=-1.0:
									# {"feature": "Bar", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[5]<=-1.0:
										return 'False'
									elif obj[5]>-1.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]>2:
								# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.4286, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Bar", "instances": 7, "metric_value": 0.381, "depth": 9}
									if obj[5]<=1.0:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[5]>1.0:
										return 'True'
									else: return 'True'
								elif obj[7]>1.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 2258, "metric_value": 0.4643, "depth": 2}
		if obj[5]>0.0:
			# {"feature": "Time", "instances": 1296, "metric_value": 0.4911, "depth": 3}
			if obj[1]>0:
				# {"feature": "Passanger", "instances": 933, "metric_value": 0.4879, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Coffeehouse", "instances": 743, "metric_value": 0.4889, "depth": 5}
					if obj[6]>1.0:
						# {"feature": "Restaurant20to50", "instances": 409, "metric_value": 0.4944, "depth": 6}
						if obj[7]<=2.0:
							# {"feature": "Education", "instances": 342, "metric_value": 0.4925, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Occupation", "instances": 258, "metric_value": 0.4826, "depth": 8}
								if obj[4]>5:
									# {"feature": "Distance", "instances": 167, "metric_value": 0.4785, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 123, "metric_value": 0.4944, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[9]>2:
										# {"feature": "Direction_same", "instances": 44, "metric_value": 0.4339, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=5:
									# {"feature": "Distance", "instances": 91, "metric_value": 0.4667, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 60, "metric_value": 0.4856, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 31, "metric_value": 0.3871, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[3]>2:
								# {"feature": "Occupation", "instances": 84, "metric_value": 0.4264, "depth": 8}
								if obj[4]>5:
									# {"feature": "Distance", "instances": 64, "metric_value": 0.416, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 48, "metric_value": 0.4296, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										# {"feature": "Direction_same", "instances": 16, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]<=5:
									# {"feature": "Direction_same", "instances": 20, "metric_value": 0.4118, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 17, "metric_value": 0.4759, "depth": 10}
										if obj[9]>1:
											return 'True'
										elif obj[9]<=1:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[7]>2.0:
							# {"feature": "Occupation", "instances": 67, "metric_value": 0.4501, "depth": 7}
							if obj[4]<=17:
								# {"feature": "Education", "instances": 63, "metric_value": 0.4717, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Distance", "instances": 49, "metric_value": 0.4783, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 26, "metric_value": 0.4583, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 23, "metric_value": 0.4522, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>3:
									# {"feature": "Distance", "instances": 14, "metric_value": 0.3393, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2083, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[4]>17:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]<=1.0:
						# {"feature": "Education", "instances": 334, "metric_value": 0.4654, "depth": 6}
						if obj[3]>0:
							# {"feature": "Restaurant20to50", "instances": 219, "metric_value": 0.4311, "depth": 7}
							if obj[7]<=2.0:
								# {"feature": "Direction_same", "instances": 215, "metric_value": 0.4335, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Occupation", "instances": 188, "metric_value": 0.4427, "depth": 9}
									if obj[4]>2.8018865567551456:
										# {"feature": "Distance", "instances": 151, "metric_value": 0.425, "depth": 10}
										if obj[9]>1:
											return 'False'
										elif obj[9]<=1:
											return 'False'
										else: return 'False'
									elif obj[4]<=2.8018865567551456:
										# {"feature": "Distance", "instances": 37, "metric_value": 0.4994, "depth": 10}
										if obj[9]>1:
											return 'False'
										elif obj[9]<=1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]>0:
									# {"feature": "Occupation", "instances": 27, "metric_value": 0.2729, "depth": 9}
									if obj[4]>4:
										# {"feature": "Distance", "instances": 19, "metric_value": 0.3792, "depth": 10}
										if obj[9]>1:
											return 'False'
										elif obj[9]<=1:
											return 'False'
										else: return 'False'
									elif obj[4]<=4:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]>2.0:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							# {"feature": "Occupation", "instances": 115, "metric_value": 0.479, "depth": 7}
							if obj[4]>5:
								# {"feature": "Restaurant20to50", "instances": 77, "metric_value": 0.4753, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Distance", "instances": 72, "metric_value": 0.4825, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 49, "metric_value": 0.4548, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 23, "metric_value": 0.4174, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[7]>2.0:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2, "depth": 9}
									if obj[8]<=0:
										return 'False'
									elif obj[8]>0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[9]<=1:
											return 'False'
										elif obj[9]>1:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[4]<=5:
								# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.417, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Direction_same", "instances": 29, "metric_value": 0.484, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 27, "metric_value": 0.4825, "depth": 10}
										if obj[9]<=2:
											return 'False'
										elif obj[9]>2:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=2:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]<=0.0:
									# {"feature": "Distance", "instances": 9, "metric_value": 0.1481, "depth": 9}
									if obj[9]<=2:
										return 'False'
									elif obj[9]>2:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Occupation", "instances": 190, "metric_value": 0.4413, "depth": 5}
					if obj[4]<=19.70715618872958:
						# {"feature": "Coffeehouse", "instances": 179, "metric_value": 0.4572, "depth": 6}
						if obj[6]>1.0:
							# {"feature": "Restaurant20to50", "instances": 98, "metric_value": 0.4155, "depth": 7}
							if obj[7]<=3.0:
								# {"feature": "Distance", "instances": 93, "metric_value": 0.4014, "depth": 8}
								if obj[9]>1:
									# {"feature": "Education", "instances": 82, "metric_value": 0.4254, "depth": 9}
									if obj[3]<=3:
										# {"feature": "Direction_same", "instances": 79, "metric_value": 0.4416, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]>3:
										return 'True'
									else: return 'True'
								elif obj[9]<=1:
									# {"feature": "Education", "instances": 11, "metric_value": 0.1558, "depth": 9}
									if obj[3]>0:
										# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]>3.0:
								# {"feature": "Education", "instances": 5, "metric_value": 0.0, "depth": 8}
								if obj[3]>2:
									return 'False'
								elif obj[3]<=2:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[6]<=1.0:
							# {"feature": "Restaurant20to50", "instances": 81, "metric_value": 0.4778, "depth": 7}
							if obj[7]<=1.0:
								# {"feature": "Distance", "instances": 58, "metric_value": 0.4855, "depth": 8}
								if obj[9]>1:
									# {"feature": "Education", "instances": 48, "metric_value": 0.4896, "depth": 9}
									if obj[3]<=2:
										# {"feature": "Direction_same", "instances": 44, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[3]>2:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]<=1:
									# {"feature": "Education", "instances": 10, "metric_value": 0.4, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]>1.0:
								# {"feature": "Distance", "instances": 23, "metric_value": 0.3581, "depth": 8}
								if obj[9]>1:
									# {"feature": "Education", "instances": 17, "metric_value": 0.4471, "depth": 9}
									if obj[3]>0:
										# {"feature": "Direction_same", "instances": 12, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]>19.70715618872958:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Passanger", "instances": 363, "metric_value": 0.4495, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Distance", "instances": 333, "metric_value": 0.4386, "depth": 5}
					if obj[9]<=1:
						# {"feature": "Restaurant20to50", "instances": 170, "metric_value": 0.3751, "depth": 6}
						if obj[7]<=1.0:
							# {"feature": "Coffeehouse", "instances": 102, "metric_value": 0.4339, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Occupation", "instances": 81, "metric_value": 0.4508, "depth": 8}
								if obj[4]>5:
									# {"feature": "Education", "instances": 50, "metric_value": 0.4767, "depth": 9}
									if obj[3]<=3:
										# {"feature": "Direction_same", "instances": 48, "metric_value": 0.4965, "depth": 10}
										if obj[8]<=1:
											return 'True'
										else: return 'True'
									elif obj[3]>3:
										return 'True'
									else: return 'True'
								elif obj[4]<=5:
									# {"feature": "Education", "instances": 31, "metric_value": 0.3653, "depth": 9}
									if obj[3]>0:
										# {"feature": "Direction_same", "instances": 22, "metric_value": 0.4339, "depth": 10}
										if obj[8]<=1:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1975, "depth": 10}
										if obj[8]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]>2.0:
								# {"feature": "Education", "instances": 21, "metric_value": 0.2721, "depth": 8}
								if obj[3]>1:
									# {"feature": "Occupation", "instances": 14, "metric_value": 0.3429, "depth": 9}
									if obj[4]<=7:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.48, "depth": 10}
										if obj[8]<=1:
											return 'True'
										else: return 'True'
									elif obj[4]>7:
										return 'True'
									else: return 'True'
								elif obj[3]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]>1.0:
							# {"feature": "Education", "instances": 68, "metric_value": 0.2603, "depth": 7}
							if obj[3]>1:
								# {"feature": "Occupation", "instances": 40, "metric_value": 0.1636, "depth": 8}
								if obj[4]>8:
									# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.2773, "depth": 9}
									if obj[6]<=3.0:
										# {"feature": "Direction_same", "instances": 20, "metric_value": 0.255, "depth": 10}
										if obj[8]<=1:
											return 'True'
										else: return 'True'
									elif obj[6]>3.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]<=8:
									return 'True'
								else: return 'True'
							elif obj[3]<=1:
								# {"feature": "Occupation", "instances": 28, "metric_value": 0.2313, "depth": 8}
								if obj[4]>5:
									# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.1633, "depth": 9}
									if obj[6]<=2.0:
										# {"feature": "Direction_same", "instances": 14, "metric_value": 0.2449, "depth": 10}
										if obj[8]<=1:
											return 'True'
										else: return 'True'
									elif obj[6]>2.0:
										return 'True'
									else: return 'True'
								elif obj[4]<=5:
									# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.2381, "depth": 9}
									if obj[6]<=2.0:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 10}
										if obj[8]<=1:
											return 'False'
										else: return 'False'
									elif obj[6]>2.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[9]>1:
						# {"feature": "Restaurant20to50", "instances": 163, "metric_value": 0.4737, "depth": 6}
						if obj[7]>0.0:
							# {"feature": "Education", "instances": 140, "metric_value": 0.4638, "depth": 7}
							if obj[3]<=3:
								# {"feature": "Direction_same", "instances": 130, "metric_value": 0.475, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Occupation", "instances": 128, "metric_value": 0.4767, "depth": 9}
									if obj[4]<=13.844008971972023:
										# {"feature": "Coffeehouse", "instances": 107, "metric_value": 0.4879, "depth": 10}
										if obj[6]>1.0:
											return 'True'
										elif obj[6]<=1.0:
											return 'True'
										else: return 'True'
									elif obj[4]>13.844008971972023:
										# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.3878, "depth": 10}
										if obj[6]>0.0:
											return 'True'
										elif obj[6]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>0:
									return 'False'
								else: return 'False'
							elif obj[3]>3:
								# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.1333, "depth": 8}
								if obj[6]>0.0:
									return 'True'
								elif obj[6]<=0.0:
									# {"feature": "Occupation", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[4]>2:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]<=0.0:
							# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.4099, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Education", "instances": 16, "metric_value": 0.3254, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Occupation", "instances": 9, "metric_value": 0.1111, "depth": 9}
									if obj[4]>3:
										return 'False'
									elif obj[4]<=3:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>2:
									# {"feature": "Occupation", "instances": 7, "metric_value": 0.3429, "depth": 9}
									if obj[4]<=12:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[4]>12:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]>2.0:
								# {"feature": "Occupation", "instances": 7, "metric_value": 0.2143, "depth": 8}
								if obj[4]<=6:
									# {"feature": "Education", "instances": 4, "metric_value": 0.0, "depth": 9}
									if obj[3]>0:
										return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								elif obj[4]>6:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[0]>1:
					# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.35, "depth": 5}
					if obj[7]>0.0:
						# {"feature": "Occupation", "instances": 28, "metric_value": 0.3333, "depth": 6}
						if obj[4]<=14:
							# {"feature": "Education", "instances": 21, "metric_value": 0.375, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.4219, "depth": 8}
								if obj[6]>1.0:
									# {"feature": "Distance", "instances": 8, "metric_value": 0.375, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]<=1:
										return 'True'
									else: return 'True'
								elif obj[6]<=1.0:
									# {"feature": "Distance", "instances": 8, "metric_value": 0.3, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.4, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[3]>2:
								return 'False'
							else: return 'False'
						elif obj[4]>14:
							return 'False'
						else: return 'False'
					elif obj[7]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[5]<=0.0:
			# {"feature": "Restaurant20to50", "instances": 962, "metric_value": 0.4124, "depth": 3}
			if obj[7]<=2.0:
				# {"feature": "Distance", "instances": 914, "metric_value": 0.4034, "depth": 4}
				if obj[9]<=2:
					# {"feature": "Coffeehouse", "instances": 746, "metric_value": 0.423, "depth": 5}
					if obj[6]<=3.0:
						# {"feature": "Occupation", "instances": 703, "metric_value": 0.4307, "depth": 6}
						if obj[4]>1.302144119170582:
							# {"feature": "Education", "instances": 535, "metric_value": 0.4453, "depth": 7}
							if obj[3]>0:
								# {"feature": "Time", "instances": 366, "metric_value": 0.4225, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 243, "metric_value": 0.3874, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Passanger", "instances": 219, "metric_value": 0.4188, "depth": 10}
										if obj[0]<=2:
											return 'False'
										elif obj[0]>2:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										# {"feature": "Passanger", "instances": 24, "metric_value": 0.0417, "depth": 10}
										if obj[0]<=1:
											return 'False'
										elif obj[0]>1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]<=0:
									# {"feature": "Passanger", "instances": 123, "metric_value": 0.4629, "depth": 9}
									if obj[0]>0:
										# {"feature": "Direction_same", "instances": 113, "metric_value": 0.4733, "depth": 10}
										if obj[8]>0:
											return 'False'
										elif obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[0]<=0:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[3]<=0:
								# {"feature": "Passanger", "instances": 169, "metric_value": 0.4772, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Time", "instances": 129, "metric_value": 0.4896, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 87, "metric_value": 0.4833, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										# {"feature": "Direction_same", "instances": 42, "metric_value": 0.4818, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[0]>1:
									# {"feature": "Time", "instances": 40, "metric_value": 0.408, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Direction_same", "instances": 25, "metric_value": 0.4608, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]>3:
										# {"feature": "Direction_same", "instances": 15, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]<=1.302144119170582:
							# {"feature": "Education", "instances": 168, "metric_value": 0.3565, "depth": 7}
							if obj[3]<=4:
								# {"feature": "Time", "instances": 164, "metric_value": 0.3511, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Passanger", "instances": 86, "metric_value": 0.3908, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Direction_same", "instances": 64, "metric_value": 0.3584, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[0]>1:
										# {"feature": "Direction_same", "instances": 22, "metric_value": 0.4502, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Direction_same", "instances": 78, "metric_value": 0.2774, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Passanger", "instances": 72, "metric_value": 0.2519, "depth": 10}
										if obj[0]>0:
											return 'False'
										elif obj[0]<=0:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										# {"feature": "Passanger", "instances": 6, "metric_value": 0.0, "depth": 10}
										if obj[0]<=1:
											return 'False'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[3]>4:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.25, "depth": 8}
								if obj[0]<=1:
									return 'True'
								elif obj[0]>1:
									# {"feature": "Time", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[1]<=0:
										return 'True'
									elif obj[1]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>3.0:
						# {"feature": "Education", "instances": 43, "metric_value": 0.2063, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Occupation", "instances": 23, "metric_value": 0.3327, "depth": 7}
							if obj[4]<=7:
								# {"feature": "Direction_same", "instances": 12, "metric_value": 0.35, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Time", "instances": 10, "metric_value": 0.3429, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Passanger", "instances": 7, "metric_value": 0.4762, "depth": 10}
										if obj[0]>1:
											return 'False'
										elif obj[0]<=1:
											return 'False'
										else: return 'False'
									elif obj[1]>3:
										return 'False'
									else: return 'False'
								elif obj[8]>0:
									return 'True'
								else: return 'True'
							elif obj[4]>7:
								# {"feature": "Passanger", "instances": 11, "metric_value": 0.0909, "depth": 8}
								if obj[0]>0:
									return 'False'
								elif obj[0]<=0:
									# {"feature": "Time", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[1]>0:
										return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[3]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[9]>2:
					# {"feature": "Passanger", "instances": 168, "metric_value": 0.2854, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Occupation", "instances": 164, "metric_value": 0.2716, "depth": 6}
						if obj[4]>0:
							# {"feature": "Education", "instances": 159, "metric_value": 0.256, "depth": 7}
							if obj[3]<=4:
								# {"feature": "Coffeehouse", "instances": 158, "metric_value": 0.2545, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Time", "instances": 111, "metric_value": 0.2183, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Direction_same", "instances": 104, "metric_value": 0.233, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]>1:
										return 'False'
									else: return 'False'
								elif obj[6]<=0.0:
									# {"feature": "Time", "instances": 47, "metric_value": 0.3288, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Direction_same", "instances": 44, "metric_value": 0.3512, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[3]>4:
								return 'True'
							else: return 'True'
						elif obj[4]<=0:
							# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.4, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Time", "instances": 4, "metric_value": 0.5, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Education", "instances": 4, "metric_value": 0.5, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]>2.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]>1:
						# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.0, "depth": 6}
						if obj[6]>-1.0:
							return 'True'
						elif obj[6]<=-1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[7]>2.0:
				# {"feature": "Education", "instances": 48, "metric_value": 0.3929, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Occupation", "instances": 25, "metric_value": 0.2743, "depth": 5}
					if obj[4]<=4:
						# {"feature": "Passanger", "instances": 14, "metric_value": 0.4286, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Time", "instances": 12, "metric_value": 0.4375, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4375, "depth": 8}
								if obj[8]>0:
									# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.25, "depth": 9}
									if obj[6]>2.0:
										return 'True'
									elif obj[6]<=2.0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=2:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[8]<=0:
									# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[6]<=2.0:
										# {"feature": "Distance", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[9]>1:
											return 'True'
										elif obj[9]<=1:
											return 'True'
										else: return 'True'
									elif obj[6]>2.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]>2:
								# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.25, "depth": 8}
								if obj[6]<=2.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=2:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]>2.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[4]>4:
						return 'True'
					else: return 'True'
				elif obj[3]>0:
					# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.3581, "depth": 5}
					if obj[6]<=2.0:
						# {"feature": "Time", "instances": 17, "metric_value": 0.4118, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Passanger", "instances": 14, "metric_value": 0.4848, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Occupation", "instances": 11, "metric_value": 0.4848, "depth": 8}
								if obj[4]>5:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 6, "metric_value": 0.5, "depth": 10}
										if obj[9]>1:
											return 'True'
										elif obj[9]<=1:
											return 'True'
										else: return 'True'
									elif obj[8]>0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=2:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]<=5:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[9]<=1:
											return 'True'
										elif obj[9]>1:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]>2:
								# {"feature": "Occupation", "instances": 3, "metric_value": 0.3333, "depth": 8}
								if obj[4]>5:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=2:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=5:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]>3:
							return 'False'
						else: return 'False'
					elif obj[6]>2.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'False'

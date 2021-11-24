def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coffeehouse", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[8]<=1.0:
		# {"feature": "Occupation", "instances": 43, "metric_value": 0.9523, "depth": 2}
		if obj[6]<=7:
			# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 3}
			if obj[2]>1:
				# {"feature": "Time", "instances": 17, "metric_value": 0.9367, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[7]<=1.0:
						# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[5]<=2:
							# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[9]>0.0:
								# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]>0:
									return 'True'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							elif obj[9]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					elif obj[7]>1.0:
						return 'False'
					else: return 'False'
				elif obj[1]>1:
					# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[5]<=2:
						return 'True'
					elif obj[5]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=1:
				# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[7]<=1.0:
					return 'False'
				elif obj[7]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]>7:
			# {"feature": "Education", "instances": 20, "metric_value": 0.7219, "depth": 3}
			if obj[5]<=2:
				# {"feature": "Gender", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[3]>0:
					# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]<=0:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[9]>0.0:
						return 'True'
					elif obj[9]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[8]>1.0:
		# {"feature": "Restaurant20to50", "instances": 42, "metric_value": 0.7919, "depth": 2}
		if obj[9]<=2.0:
			# {"feature": "Direction_same", "instances": 39, "metric_value": 0.679, "depth": 3}
			if obj[10]<=0:
				# {"feature": "Coupon", "instances": 27, "metric_value": 0.8256, "depth": 4}
				if obj[2]>0:
					# {"feature": "Age", "instances": 25, "metric_value": 0.7219, "depth": 5}
					if obj[4]<=3:
						# {"feature": "Gender", "instances": 17, "metric_value": 0.874, "depth": 6}
						if obj[3]>0:
							# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 7}
							if obj[6]<=14:
								return 'True'
							elif obj[6]>14:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]>2:
									return 'True'
								elif obj[0]<=2:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1]<=0:
										return 'True'
									elif obj[1]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[3]<=0:
							# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[1]>2:
								# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[6]<=12:
									return 'True'
								elif obj[6]>12:
									return 'False'
								else: return 'False'
							elif obj[1]<=2:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]>3:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[10]>0:
				return 'True'
			else: return 'True'
		elif obj[9]>2.0:
			return 'False'
		else: return 'False'
	else: return 'True'

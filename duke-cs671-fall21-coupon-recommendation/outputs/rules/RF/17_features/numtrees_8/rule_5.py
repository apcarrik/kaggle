def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9899, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 83, "metric_value": 0.9949, "depth": 2}
		if obj[9]<=2:
			# {"feature": "Gender", "instances": 59, "metric_value": 0.9898, "depth": 3}
			if obj[5]>0:
				# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.99, "depth": 4}
				if obj[14]<=2.0:
					# {"feature": "Bar", "instances": 31, "metric_value": 0.9629, "depth": 5}
					if obj[12]<=1.0:
						# {"feature": "Time", "instances": 24, "metric_value": 0.8709, "depth": 6}
						if obj[2]>0:
							# {"feature": "Distance", "instances": 16, "metric_value": 0.9887, "depth": 7}
							if obj[16]>1:
								# {"feature": "Income", "instances": 12, "metric_value": 0.8113, "depth": 8}
								if obj[11]>2:
									# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[6]>2:
										return 'False'
									elif obj[6]<=2:
										return 'True'
									else: return 'True'
								elif obj[11]<=2:
									return 'False'
								else: return 'False'
							elif obj[16]<=1:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[12]>1.0:
						# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[3]<=3:
							return 'True'
						elif obj[3]>3:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>0:
								return 'False'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[14]>2.0:
					return 'True'
				else: return 'True'
			elif obj[5]<=0:
				# {"feature": "Children", "instances": 25, "metric_value": 0.8555, "depth": 4}
				if obj[8]<=0:
					# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.9495, "depth": 5}
					if obj[13]<=3.0:
						# {"feature": "Occupation", "instances": 17, "metric_value": 0.874, "depth": 6}
						if obj[10]<=7:
							# {"feature": "Distance", "instances": 13, "metric_value": 0.9612, "depth": 7}
							if obj[16]<=1:
								# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[14]>0.0:
									# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[2]<=3:
										return 'False'
									elif obj[2]>3:
										return 'True'
									else: return 'True'
								elif obj[14]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[16]>1:
								# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[1]<=1:
									return 'True'
								elif obj[1]>1:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[2]<=1:
										return 'False'
									elif obj[2]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[10]>7:
							return 'True'
						else: return 'True'
					elif obj[13]>3.0:
						return 'False'
					else: return 'False'
				elif obj[8]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[9]>2:
			# {"feature": "Time", "instances": 24, "metric_value": 0.7383, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[10]>1:
					# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[3]>0:
						# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[12]>0.0:
							# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[6]<=4:
								return 'False'
							elif obj[6]>4:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[15]<=0:
									return 'False'
								elif obj[15]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[12]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[10]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Children", "instances": 44, "metric_value": 0.8113, "depth": 2}
		if obj[8]<=0:
			# {"feature": "Coffeehouse", "instances": 29, "metric_value": 0.5788, "depth": 3}
			if obj[13]<=3.0:
				# {"feature": "Maritalstatus", "instances": 27, "metric_value": 0.3809, "depth": 4}
				if obj[7]<=1:
					return 'True'
				elif obj[7]>1:
					# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[12]<=0.0:
						return 'True'
					elif obj[12]>0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[13]>3.0:
				return 'False'
			else: return 'False'
		elif obj[8]>0:
			# {"feature": "Age", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[6]>1:
				# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[9]<=1:
					return 'False'
				elif obj[9]>1:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]<=2:
						return 'True'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'

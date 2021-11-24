def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon_validity", "instances": 72, "metric_value": 0.9978, "depth": 2}
		if obj[4]<=0:
			# {"feature": "Coffeehouse", "instances": 38, "metric_value": 0.9678, "depth": 3}
			if obj[12]>0.0:
				# {"feature": "Income", "instances": 26, "metric_value": 0.7793, "depth": 4}
				if obj[10]<=7:
					# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.65, "depth": 5}
					if obj[13]>1.0:
						return 'True'
					elif obj[13]<=1.0:
						# {"feature": "Bar", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[11]>0.0:
							# {"feature": "Children", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[7]>0:
								# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[9]<=6:
									return 'True'
								elif obj[9]>6:
									return 'False'
								else: return 'False'
							elif obj[7]<=0:
								return 'False'
							else: return 'False'
						elif obj[11]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[10]>7:
					return 'False'
				else: return 'False'
			elif obj[12]<=0.0:
				# {"feature": "Weather", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[11]<=2.0:
						# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[9]>2:
							return 'False'
						elif obj[9]<=2:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=1:
								return 'True'
							elif obj[2]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[11]>2.0:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>0:
			# {"feature": "Education", "instances": 34, "metric_value": 0.9082, "depth": 3}
			if obj[8]>1:
				# {"feature": "Coupon", "instances": 20, "metric_value": 0.469, "depth": 4}
				if obj[3]>2:
					return 'False'
				elif obj[3]<=2:
					# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[11]>0.0:
						return 'False'
					elif obj[11]<=0.0:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=1:
							return 'True'
						elif obj[2]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[8]<=1:
				# {"feature": "Bar", "instances": 14, "metric_value": 0.9403, "depth": 4}
				if obj[11]<=1.0:
					# {"feature": "Age", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[6]<=6:
						# {"feature": "Time", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]>0:
								return 'False'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>6:
						return 'False'
					else: return 'False'
				elif obj[11]>1.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Education", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[8]<=2:
			return 'True'
		elif obj[8]>2:
			# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[5]>0:
				return 'False'
			elif obj[5]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'

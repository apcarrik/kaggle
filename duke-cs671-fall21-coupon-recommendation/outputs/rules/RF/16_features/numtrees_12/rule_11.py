def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Time", "instances": 85, "metric_value": 0.971, "depth": 1}
	if obj[2]>1:
		# {"feature": "Bar", "instances": 44, "metric_value": 0.8113, "depth": 2}
		if obj[11]<=1.0:
			# {"feature": "Coupon", "instances": 33, "metric_value": 0.9183, "depth": 3}
			if obj[3]>1:
				# {"feature": "Income", "instances": 25, "metric_value": 0.7219, "depth": 4}
				if obj[10]>3:
					return 'True'
				elif obj[10]<=3:
					# {"feature": "Age", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[6]<=4:
						# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[7]<=0:
							# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[12]<=1.0:
								return 'False'
							elif obj[12]>1.0:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=0:
									return 'False'
								elif obj[0]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[7]>0:
							return 'True'
						else: return 'True'
					elif obj[6]>4:
						# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[12]<=2.0:
							return 'True'
						elif obj[12]>2.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[3]<=1:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[9]<=7:
					# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]>2:
							return 'True'
						elif obj[6]<=2:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[9]>7:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[11]>1.0:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Coffeehouse", "instances": 41, "metric_value": 0.9892, "depth": 2}
		if obj[12]<=2.0:
			# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Income", "instances": 21, "metric_value": 0.8631, "depth": 4}
				if obj[10]>1:
					# {"feature": "Weather", "instances": 16, "metric_value": 0.5436, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[6]<=3:
							return 'True'
						elif obj[6]>3:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[10]<=1:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]>3:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[9]<=5:
					# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[7]<=0:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[6]<=3:
							return 'True'
						elif obj[6]>3:
							return 'False'
						else: return 'False'
					elif obj[7]>0:
						return 'False'
					else: return 'False'
				elif obj[9]>5:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[12]>2.0:
			return 'False'
		else: return 'False'
	else: return 'False'

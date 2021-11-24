def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[2]>1:
		# {"feature": "Time", "instances": 66, "metric_value": 0.9327, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Income", "instances": 39, "metric_value": 0.9995, "depth": 3}
			if obj[9]<=5:
				# {"feature": "Occupation", "instances": 28, "metric_value": 0.9403, "depth": 4}
				if obj[8]>6:
					# {"feature": "Bar", "instances": 17, "metric_value": 0.9975, "depth": 5}
					if obj[10]<=1.0:
						# {"feature": "Age", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[5]>1:
							# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[13]<=0:
									return 'False'
								elif obj[13]>0:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[10]>1.0:
						# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[5]<=4:
							return 'False'
						elif obj[5]>4:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[8]<=6:
					# {"feature": "Children", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[6]<=0:
						return 'True'
					elif obj[6]>0:
						# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[9]>5:
				# {"feature": "Direction_same", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[13]<=0:
					return 'False'
				elif obj[13]>0:
					# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]<=0:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=4:
							return 'True'
						elif obj[5]>4:
							return 'False'
						else: return 'False'
					elif obj[4]>0:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]>1:
			# {"feature": "Occupation", "instances": 27, "metric_value": 0.6052, "depth": 3}
			if obj[8]<=18:
				# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.258, "depth": 4}
				if obj[12]>0.0:
					return 'True'
				elif obj[12]<=0.0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]>18:
				# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[5]<=6:
					return 'False'
				elif obj[5]>6:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Coupon_validity", "instances": 19, "metric_value": 0.6292, "depth": 2}
		if obj[3]<=0:
			return 'False'
		elif obj[3]>0:
			# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[7]>0:
				# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[4]>0:
					return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			elif obj[7]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'

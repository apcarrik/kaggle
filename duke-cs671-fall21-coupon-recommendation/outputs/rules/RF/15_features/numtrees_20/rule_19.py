def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Income", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[9]>1:
		# {"feature": "Restaurant20to50", "instances": 47, "metric_value": 0.9839, "depth": 2}
		if obj[12]<=1.0:
			# {"feature": "Coupon", "instances": 36, "metric_value": 1.0, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Coupon_validity", "instances": 22, "metric_value": 0.9457, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Children", "instances": 16, "metric_value": 1.0, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[10]<=1.0:
							# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[5]<=4:
								return 'False'
							elif obj[5]>4:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1]>0:
										return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[10]>1.0:
							return 'True'
						else: return 'True'
					elif obj[6]>0:
						# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[8]<=8:
							return 'True'
						elif obj[8]>8:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]>0:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				# {"feature": "Time", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[1]>1:
					# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[3]>0:
						# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[6]<=0:
							return 'False'
						elif obj[6]>0:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[12]>1.0:
			# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[11]<=2.0:
				# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[7]>0:
					return 'True'
				elif obj[7]<=0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[11]>2.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[9]<=1:
		return 'False'
	else: return 'False'

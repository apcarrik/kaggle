def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[3]<=3:
		# {"feature": "Income", "instances": 33, "metric_value": 0.9457, "depth": 2}
		if obj[10]<=6:
			# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.8404, "depth": 3}
			if obj[12]<=2.0:
				# {"feature": "Age", "instances": 21, "metric_value": 0.7025, "depth": 4}
				if obj[6]>0:
					# {"feature": "Distance", "instances": 17, "metric_value": 0.5226, "depth": 5}
					if obj[15]<=1:
						# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[8]>0:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[13]>1.0:
								return 'True'
							elif obj[13]<=1.0:
								# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[9]<=8:
									return 'False'
								elif obj[9]>8:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[8]<=0:
							return 'True'
						else: return 'True'
					elif obj[15]>1:
						return 'True'
					else: return 'True'
				elif obj[6]<=0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[12]>2.0:
				# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[8]>1:
						return 'True'
					elif obj[8]<=1:
						return 'False'
					else: return 'False'
				elif obj[5]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[10]>6:
			# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[2]<=3:
				return 'False'
			elif obj[2]>3:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[6]<=4:
					return 'True'
				elif obj[6]>4:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[3]>3:
		# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.7642, "depth": 2}
		if obj[12]<=1.0:
			return 'False'
		elif obj[12]>1.0:
			# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[5]>0:
					return 'False'
				elif obj[5]<=0:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'

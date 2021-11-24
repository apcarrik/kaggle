def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[3]>0:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.8936, "depth": 2}
		if obj[9]>1:
			# {"feature": "Bar", "instances": 25, "metric_value": 0.9427, "depth": 3}
			if obj[11]<=2.0:
				# {"feature": "Time", "instances": 22, "metric_value": 0.976, "depth": 4}
				if obj[2]>0:
					# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.9968, "depth": 5}
					if obj[13]>0.0:
						# {"feature": "Gender", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[5]>0:
							# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[8]<=2:
								# {"feature": "Income", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[10]<=1:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[0]<=2:
										return 'False'
									elif obj[0]>2:
										return 'True'
									else: return 'True'
								elif obj[10]>1:
									return 'True'
								else: return 'True'
							elif obj[8]>2:
								return 'False'
							else: return 'False'
						elif obj[5]<=0:
							return 'False'
						else: return 'False'
					elif obj[13]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[8]>0:
						return 'True'
					elif obj[8]<=0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[11]>2.0:
				return 'True'
			else: return 'True'
		elif obj[9]<=1:
			return 'True'
		else: return 'True'
	elif obj[3]<=0:
		# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[2]<=3:
			return 'False'
		elif obj[2]>3:
			return 'True'
		else: return 'True'
	else: return 'False'

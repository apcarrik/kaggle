def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[12]<=2.0:
		# {"feature": "Income", "instances": 30, "metric_value": 0.971, "depth": 2}
		if obj[9]<=7:
			# {"feature": "Gender", "instances": 28, "metric_value": 0.9403, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Passanger", "instances": 17, "metric_value": 0.9975, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[8]>2:
						# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[2]>1:
							# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[5]<=4:
								return 'False'
							elif obj[5]>4:
								# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]>0:
									return 'False'
								elif obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[2]<=1:
							# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=0:
								return 'True'
							elif obj[3]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[8]<=2:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[4]>0:
				# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[11]<=2.0:
					# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=0:
							return 'True'
						elif obj[1]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[11]>2.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]>7:
			return 'True'
		else: return 'True'
	elif obj[12]>2.0:
		return 'True'
	else: return 'True'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Children", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[7]<=0:
		# {"feature": "Age", "instances": 26, "metric_value": 0.8404, "depth": 2}
		if obj[6]<=5:
			# {"feature": "Time", "instances": 23, "metric_value": 0.6666, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[9]>5:
					# {"feature": "Coupon_validity", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[4]<=0:
						# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=0:
							return 'True'
						elif obj[5]>0:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=1:
								return 'False'
							elif obj[3]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]>0:
						return 'False'
					else: return 'False'
				elif obj[9]<=5:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				return 'True'
			else: return 'True'
		elif obj[6]>5:
			return 'False'
		else: return 'False'
	elif obj[7]>0:
		# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.971, "depth": 2}
		if obj[13]<=1.0:
			# {"feature": "Age", "instances": 17, "metric_value": 0.7871, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[15]>1:
					# {"feature": "Coupon_validity", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[4]>0:
						# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[9]>2:
							# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[12]<=0.0:
								return 'False'
							elif obj[12]>0.0:
								return 'True'
							else: return 'True'
						elif obj[9]<=2:
							return 'True'
						else: return 'True'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				elif obj[15]<=1:
					return 'False'
				else: return 'False'
			elif obj[6]>2:
				return 'False'
			else: return 'False'
		elif obj[13]>1.0:
			# {"feature": "Weather", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

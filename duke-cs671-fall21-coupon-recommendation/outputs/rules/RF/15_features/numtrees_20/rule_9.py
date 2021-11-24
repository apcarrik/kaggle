def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[12]<=1.0:
		# {"feature": "Gender", "instances": 31, "metric_value": 0.9383, "depth": 2}
		if obj[4]>0:
			# {"feature": "Passanger", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[8]<=6:
					# {"feature": "Income", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[9]<=4:
						# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=1:
							return 'False'
						elif obj[1]>1:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=2:
								return 'True'
							elif obj[2]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[9]>4:
						return 'True'
					else: return 'True'
				elif obj[8]>6:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[4]<=0:
			# {"feature": "Age", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[5]>0:
				# {"feature": "Distance", "instances": 14, "metric_value": 0.3712, "depth": 4}
				if obj[14]<=2:
					return 'False'
				elif obj[14]>2:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>1:
						return 'False'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[12]>1.0:
		# {"feature": "Bar", "instances": 20, "metric_value": 0.7219, "depth": 2}
		if obj[10]>1.0:
			return 'True'
		elif obj[10]<=1.0:
			# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[1]>0:
				# {"feature": "Income", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[9]>3:
					return 'True'
				elif obj[9]<=3:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Income", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[9]<=7:
		# {"feature": "Coupon", "instances": 46, "metric_value": 0.9986, "depth": 2}
		if obj[2]>0:
			# {"feature": "Education", "instances": 41, "metric_value": 0.9789, "depth": 3}
			if obj[7]>1:
				# {"feature": "Time", "instances": 22, "metric_value": 0.994, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Passanger", "instances": 20, "metric_value": 0.971, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Children", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[6]<=0:
							return 'False'
						elif obj[6]>0:
							# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=3:
								return 'True'
							elif obj[5]>3:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]>1:
						# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[7]<=1:
				# {"feature": "Occupation", "instances": 19, "metric_value": 0.8315, "depth": 4}
				if obj[8]>2:
					# {"feature": "Age", "instances": 17, "metric_value": 0.6723, "depth": 5}
					if obj[5]<=6:
						# {"feature": "Children", "instances": 16, "metric_value": 0.5436, "depth": 6}
						if obj[6]<=0:
							return 'True'
						elif obj[6]>0:
							# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[4]>0:
								return 'True'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]>6:
						return 'False'
					else: return 'False'
				elif obj[8]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[9]>7:
		return 'True'
	else: return 'True'

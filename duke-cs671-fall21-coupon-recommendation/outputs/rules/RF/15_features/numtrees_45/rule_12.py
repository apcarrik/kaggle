def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Age", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[5]>0:
			# {"feature": "Passanger", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[12]<=1.0:
					# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[8]<=11:
						# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[6]<=0:
							return 'True'
						elif obj[6]>0:
							# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]>0:
								return 'True'
							elif obj[3]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[8]>11:
						return 'False'
					else: return 'False'
				elif obj[12]>1.0:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		elif obj[5]<=0:
			# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]>3:
		return 'False'
	else: return 'False'

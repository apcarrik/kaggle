def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[9]>2:
		# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[10]<=1.0:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[14]>1:
					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]>2:
							return 'True'
						elif obj[5]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[14]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[10]>1.0:
			return 'True'
		else: return 'True'
	elif obj[9]<=2:
		# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[12]<=1.0:
			return 'False'
		elif obj[12]>1.0:
			# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[4]>0:
				return 'False'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'

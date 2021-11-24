def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Direction_same", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[13]<=0:
		# {"feature": "Passanger", "instances": 28, "metric_value": 1.0, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Coupon", "instances": 18, "metric_value": 0.8524, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Bar", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[10]<=1.0:
					# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[7]<=1:
						return 'True'
					elif obj[7]>1:
						# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=0:
							return 'False'
						elif obj[4]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[10]>1.0:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[8]<=9:
				return 'True'
			elif obj[8]>9:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[13]>0:
		return 'True'
	else: return 'True'

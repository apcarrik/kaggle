def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[9]>2:
		# {"feature": "Age", "instances": 28, "metric_value": 1.0, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Children", "instances": 17, "metric_value": 0.9367, "depth": 3}
			if obj[7]>0:
				# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[8]>0:
					return 'True'
				elif obj[8]<=0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]<=0:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[0]>0:
					# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]>2:
			# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[3]<=3:
					# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[8]>0:
							return 'True'
						elif obj[8]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]>3:
					return 'False'
				else: return 'False'
			elif obj[2]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[9]<=2:
		return 'False'
	else: return 'False'

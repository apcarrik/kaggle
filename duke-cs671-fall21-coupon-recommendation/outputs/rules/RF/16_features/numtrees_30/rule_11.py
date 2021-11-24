def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[2]>0:
		# {"feature": "Income", "instances": 26, "metric_value": 0.9829, "depth": 2}
		if obj[10]>2:
			# {"feature": "Coupon", "instances": 22, "metric_value": 0.9024, "depth": 3}
			if obj[3]>2:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[15]>1:
					return 'True'
				elif obj[15]<=1:
					# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[8]>0:
						return 'True'
					elif obj[8]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]<=2:
				# {"feature": "Gender", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[5]>0:
					# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						return 'False'
					else: return 'False'
				elif obj[5]<=0:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[9]<=5:
						return 'False'
					elif obj[9]>5:
						# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]<=0:
							return 'False'
						elif obj[6]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[10]<=2:
			return 'False'
		else: return 'False'
	elif obj[2]<=0:
		return 'True'
	else: return 'True'

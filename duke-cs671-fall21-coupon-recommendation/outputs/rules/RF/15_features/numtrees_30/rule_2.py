def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.8905, "depth": 2}
		if obj[11]<=1.0:
			# {"feature": "Occupation", "instances": 14, "metric_value": 1.0, "depth": 3}
			if obj[8]<=13:
				# {"feature": "Age", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[5]>2:
					# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[7]<=2:
						# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[10]<=2.0:
							return 'True'
						elif obj[10]>2.0:
							return 'False'
						else: return 'False'
					elif obj[7]>2:
						return 'False'
					else: return 'False'
				elif obj[5]<=2:
					# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]<=0:
						return 'False'
					elif obj[1]>0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'False'
						elif obj[0]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[8]>13:
				return 'True'
			else: return 'True'
		elif obj[11]>1.0:
			# {"feature": "Time", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[4]<=0:
					return 'True'
				elif obj[4]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[4]>0:
			return 'False'
		elif obj[4]<=0:
			# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

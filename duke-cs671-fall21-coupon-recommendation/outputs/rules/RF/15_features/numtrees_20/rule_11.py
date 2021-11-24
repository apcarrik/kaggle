def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Income", "instances": 51, "metric_value": 0.9183, "depth": 1}
	if obj[9]>2:
		# {"feature": "Education", "instances": 41, "metric_value": 0.8015, "depth": 2}
		if obj[7]<=2:
			# {"feature": "Coupon_validity", "instances": 30, "metric_value": 0.65, "depth": 3}
			if obj[3]<=0:
				return 'True'
			elif obj[3]>0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[8]<=6:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[2]<=1:
						return 'False'
					elif obj[2]>1:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>1:
							return 'True'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[8]>6:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[7]>2:
			# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[11]<=2.0:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[0]>0:
					# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[11]>2.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[9]<=2:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[2]>2:
			return 'False'
		elif obj[2]<=2:
			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[7]<=2:
				return 'True'
			elif obj[7]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

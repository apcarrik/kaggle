def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[2]>1:
		# {"feature": "Bar", "instances": 36, "metric_value": 0.9183, "depth": 2}
		if obj[10]<=0.0:
			# {"feature": "Age", "instances": 19, "metric_value": 0.6292, "depth": 3}
			if obj[5]<=5:
				return 'True'
			elif obj[5]>5:
				# {"feature": "Income", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[9]<=2:
					return 'True'
				elif obj[9]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[10]>0.0:
			# {"feature": "Coupon_validity", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[3]>0:
				# {"feature": "Income", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[9]>0:
					# {"feature": "Time", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[9]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]<=0:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Occupation", "instances": 15, "metric_value": 0.7219, "depth": 2}
		if obj[8]>2:
			# {"feature": "Age", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[5]<=2:
				return 'False'
			elif obj[5]>2:
				# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[7]<=0:
					# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]>1:
						return 'False'
					elif obj[1]<=1:
						# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[9]>6:
							return 'False'
						elif obj[9]<=6:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[7]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]<=2:
			return 'True'
		else: return 'True'
	else: return 'False'

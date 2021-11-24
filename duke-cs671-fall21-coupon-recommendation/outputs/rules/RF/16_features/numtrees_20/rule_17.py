def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[6]<=3:
		# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.8691, "depth": 2}
		if obj[12]>0.0:
			# {"feature": "Income", "instances": 26, "metric_value": 0.7063, "depth": 3}
			if obj[10]>3:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[3]<=3:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[9]>4:
						# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[7]<=0:
							return 'False'
						elif obj[7]>0:
							return 'True'
						else: return 'True'
					elif obj[9]<=4:
						return 'True'
					else: return 'True'
				elif obj[3]>3:
					return 'False'
				else: return 'False'
			elif obj[10]<=3:
				return 'False'
			else: return 'False'
		elif obj[12]<=0.0:
			# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[10]<=3:
				return 'True'
			elif obj[10]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[6]>3:
		# {"feature": "Education", "instances": 20, "metric_value": 0.7219, "depth": 2}
		if obj[8]>1:
			# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[11]>0.0:
				# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[11]<=0.0:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'

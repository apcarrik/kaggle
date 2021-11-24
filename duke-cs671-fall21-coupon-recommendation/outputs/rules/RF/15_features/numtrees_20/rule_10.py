def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[8]<=14:
		# {"feature": "Coupon", "instances": 47, "metric_value": 0.9918, "depth": 2}
		if obj[2]>2:
			# {"feature": "Passanger", "instances": 25, "metric_value": 0.9044, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[12]<=1.0:
					# {"feature": "Income", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[9]>4:
						# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[13]<=0:
							return 'False'
						elif obj[13]>0:
							return 'True'
						else: return 'True'
					elif obj[9]<=4:
						return 'True'
					else: return 'True'
				elif obj[12]>1.0:
					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[7]<=2:
					return 'True'
				elif obj[7]>2:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=2:
			# {"feature": "Direction_same", "instances": 22, "metric_value": 0.976, "depth": 3}
			if obj[13]<=0:
				# {"feature": "Income", "instances": 19, "metric_value": 0.8997, "depth": 4}
				if obj[9]>1:
					# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.971, "depth": 5}
					if obj[12]<=1.0:
						# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[5]>1:
									return 'True'
								elif obj[5]<=1:
									return 'False'
								else: return 'False'
							elif obj[3]>0:
								return 'False'
							else: return 'False'
						elif obj[1]>2:
							return 'False'
						else: return 'False'
					elif obj[12]>1.0:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=3:
							return 'True'
						elif obj[5]>3:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[9]<=1:
					return 'False'
				else: return 'False'
			elif obj[13]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[8]>14:
		return 'False'
	else: return 'False'

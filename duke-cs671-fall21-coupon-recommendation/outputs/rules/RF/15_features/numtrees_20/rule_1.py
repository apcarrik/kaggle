def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[5]<=6:
		# {"feature": "Bar", "instances": 47, "metric_value": 0.9997, "depth": 2}
		if obj[10]<=2.0:
			# {"feature": "Coupon", "instances": 42, "metric_value": 0.9852, "depth": 3}
			if obj[2]>2:
				# {"feature": "Coffeehouse", "instances": 24, "metric_value": 0.8709, "depth": 4}
				if obj[11]>0.0:
					# {"feature": "Occupation", "instances": 20, "metric_value": 0.7219, "depth": 5}
					if obj[8]<=7:
						# {"feature": "Income", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[9]>3:
							# {"feature": "Children", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[6]>0:
								return 'True'
							elif obj[6]<=0:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=0:
									return 'True'
								elif obj[1]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[9]<=3:
							# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[6]>0:
								return 'False'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[8]>7:
						return 'True'
					else: return 'True'
				elif obj[11]<=0.0:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[12]<=1.0:
						return 'False'
					elif obj[12]>1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=2:
				# {"feature": "Education", "instances": 18, "metric_value": 0.9641, "depth": 4}
				if obj[7]>1:
					# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.9968, "depth": 5}
					if obj[12]>0.0:
						# {"feature": "Income", "instances": 13, "metric_value": 0.9612, "depth": 6}
						if obj[9]>1:
							# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[11]<=3.0:
								return 'False'
							elif obj[11]>3.0:
								# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]>4:
									return 'True'
								elif obj[8]<=4:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[9]<=1:
							# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[11]>0.0:
								return 'True'
							elif obj[11]<=0.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[12]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[7]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[10]>2.0:
			return 'False'
		else: return 'False'
	elif obj[5]>6:
		return 'True'
	else: return 'True'

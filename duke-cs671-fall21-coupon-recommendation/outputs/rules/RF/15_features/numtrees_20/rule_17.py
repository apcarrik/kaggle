def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 46, "metric_value": 0.9945, "depth": 2}
		if obj[8]>5:
			# {"feature": "Education", "instances": 26, "metric_value": 0.8905, "depth": 3}
			if obj[7]>1:
				# {"feature": "Age", "instances": 18, "metric_value": 0.9911, "depth": 4}
				if obj[5]>1:
					# {"feature": "Bar", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[10]>0.0:
						# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=2:
								return 'True'
							elif obj[2]>2:
								# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[11]>0.0:
									return 'False'
								elif obj[11]<=0.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[10]<=0.0:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]>1:
							return 'False'
						elif obj[1]<=1:
							# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=0:
								return 'False'
							elif obj[2]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[5]<=1:
					# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]<=1:
				return 'True'
			else: return 'True'
		elif obj[8]<=5:
			# {"feature": "Education", "instances": 20, "metric_value": 0.9341, "depth": 3}
			if obj[7]<=3:
				# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.8524, "depth": 4}
				if obj[11]<=1.0:
					# {"feature": "Age", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[5]>0:
						return 'False'
					elif obj[5]<=0:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=2:
							return 'False'
						elif obj[1]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[11]>1.0:
					# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[4]<=0:
						# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[9]>0:
							return 'False'
						elif obj[9]<=0:
							return 'True'
						else: return 'True'
					elif obj[4]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[7]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=0:
		return 'True'
	else: return 'True'

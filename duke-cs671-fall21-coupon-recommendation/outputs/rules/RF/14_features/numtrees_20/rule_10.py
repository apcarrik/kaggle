def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[2]>0:
		# {"feature": "Income", "instances": 42, "metric_value": 0.9737, "depth": 2}
		if obj[8]<=3:
			# {"feature": "Bar", "instances": 25, "metric_value": 0.9896, "depth": 3}
			if obj[9]<=2.0:
				# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.9984, "depth": 4}
				if obj[10]<=1.0:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[7]<=6:
						# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[5]>0:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[0]>1:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[4]>2:
										return 'False'
									elif obj[4]<=2:
										return 'True'
									else: return 'True'
								elif obj[0]<=1:
									return 'False'
								else: return 'False'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[1]>3:
							return 'True'
						else: return 'True'
					elif obj[7]>6:
						return 'False'
					else: return 'False'
				elif obj[10]>1.0:
					# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[7]>4:
						return 'True'
					elif obj[7]<=4:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[9]>2.0:
				return 'False'
			else: return 'False'
		elif obj[8]>3:
			# {"feature": "Occupation", "instances": 17, "metric_value": 0.6723, "depth": 3}
			if obj[7]>0:
				# {"feature": "Bar", "instances": 16, "metric_value": 0.5436, "depth": 4}
				if obj[9]<=1.0:
					return 'True'
				elif obj[9]>1.0:
					# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[10]<=1.0:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[10]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[7]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Bar", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[9]<=2.0:
			return 'False'
		elif obj[9]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'

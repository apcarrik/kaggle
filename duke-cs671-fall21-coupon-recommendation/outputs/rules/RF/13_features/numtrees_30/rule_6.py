def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[12]<=2:
		# {"feature": "Occupation", "instances": 30, "metric_value": 0.9481, "depth": 2}
		if obj[7]<=12:
			# {"feature": "Coupon", "instances": 28, "metric_value": 0.9059, "depth": 3}
			if obj[2]>0:
				# {"feature": "Passanger", "instances": 21, "metric_value": 0.7919, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[9]<=1.0:
						# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[8]<=1.0:
							# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[1]>1:
								return 'True'
							elif obj[1]<=1:
								# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]>0:
										return 'True'
									elif obj[6]<=0:
										return 'False'
									else: return 'False'
								elif obj[4]>2:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[8]>1.0:
							# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]<=2:
								return 'False'
							elif obj[4]>2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[9]>1.0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[4]>2:
					# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[8]>0.0:
						return 'True'
					elif obj[8]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[4]<=2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[7]>12:
			return 'False'
		else: return 'False'
	elif obj[12]>2:
		return 'False'
	else: return 'False'

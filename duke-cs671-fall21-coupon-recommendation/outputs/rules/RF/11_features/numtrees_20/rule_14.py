def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[10]<=2:
		# {"feature": "Bar", "instances": 41, "metric_value": 0.9474, "depth": 2}
		if obj[6]<=1.0:
			# {"feature": "Age", "instances": 29, "metric_value": 0.9923, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Occupation", "instances": 18, "metric_value": 0.9641, "depth": 4}
				if obj[5]<=12:
					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[8]<=1.0:
						# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[0]>0:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[2]>0:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1]<=0:
										return 'False'
									elif obj[1]>0:
										return 'True'
									else: return 'True'
								elif obj[2]<=0:
									return 'False'
								else: return 'False'
							elif obj[4]>2:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[8]>1.0:
						return 'False'
					else: return 'False'
				elif obj[5]>12:
					# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[7]>1.0:
						return 'True'
					elif obj[7]<=1.0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[3]>2:
				# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[7]<=3.0:
					# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[5]<=9:
						return 'True'
					elif obj[5]>9:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]>1:
								return 'False'
							elif obj[2]<=1:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[7]>3.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>1.0:
			# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[8]>-1.0:
				# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[4]>0:
					return 'True'
				elif obj[4]<=0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[8]<=-1.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[10]>2:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[2]>2:
			# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[5]>2:
				# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[5]<=2:
				return 'True'
			else: return 'True'
		elif obj[2]<=2:
			return 'False'
		else: return 'False'
	else: return 'False'

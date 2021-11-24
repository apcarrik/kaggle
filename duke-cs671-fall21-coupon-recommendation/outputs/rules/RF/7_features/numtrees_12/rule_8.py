def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[6]<=2:
		# {"feature": "Education", "instances": 73, "metric_value": 0.9605, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Passanger", "instances": 61, "metric_value": 0.9127, "depth": 3}
			if obj[0]>0:
				# {"feature": "Occupation", "instances": 56, "metric_value": 0.9403, "depth": 4}
				if obj[3]>1.8168184321964107:
					# {"feature": "Restaurant20to50", "instances": 49, "metric_value": 0.9633, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Coupon", "instances": 46, "metric_value": 0.9503, "depth": 6}
						if obj[1]>0:
							# {"feature": "Direction_same", "instances": 39, "metric_value": 0.9612, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]<=0.0:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]>3:
							return 'False'
						elif obj[1]<=3:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]<=1.8168184321964107:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>1.0:
							return 'True'
						elif obj[4]<=1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]>2:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[1]>2:
				# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[0]>0:
						# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[3]<=6:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[3]>6:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[4]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[1]<=2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[6]>2:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[1]<=0:
			return 'False'
		elif obj[1]>0:
			# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[3]<=5:
				return 'True'
			elif obj[3]>5:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
